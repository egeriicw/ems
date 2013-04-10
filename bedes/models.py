from django.db import models

# Create your models here.
class Site(models.Model):
	name 		= models.CharField(blank=False, max_length=100, unique=True)
	city 		= models.CharField(blank=True, max_length=100, default=None)
	state 		= models.CharField(blank=False, max_length=100)
	county 		= models.CharField(blank=True, max_length=100, default=None)
	country 	= models.CharField(blank=False, max_length=100)
	elevation 	= models.FloatField(blank=True, null=True)
	slug 		= models.SlugField(blank=True, max_length=40)
	numfacilities = models.IntegerField(blank=True, default=0)

	def __unicode__(self):
		if self.city is None:
			return self.name + ": " + self.county + ", " + self.state + " -- " + str(self.numfacilities) + " facilities"
		else:
			return self.name + ": " + self.city + ", " + self.state + " -- " + str(self.numfacilities) + " facilities"


class ClimateZone(models.Model):
	CLIMATE_ZONE = (
		('1A', '1A, Very Hot - Humid (Miami, FL)'),
		('2A', '2A, Hot - Humid (Houston, TX)'),
		('2B', '2B, Hot - Dry (Phoenix, AZ)'),
		('3A', '3A, Warm - Humid (Memphis, TN)'),
		('3B', '3B, Warm - Dry (El Paso, TX)'),
		('3C', '3C, Warm - Marine (San Francisco, CA)'),
		('4A', '4A, Mixed - Humid (Baltimore, MD)'),
		('4B', '4B, Mixed - Dry (Albuquerque, NM)'),
		('4C', '4C, Mixed - Marine (Salem, OR)'),
		('5A', '5A, Cool - Humid (Chicago, IL)'),
		('5B', '5B, Cool - Dry (Boise, ID)'),
		('6A', '6A, Cold - Humid (Burlington, VT)'),
		('6B', '6B, Cold - Dry (Helena, MT)'),
		('7', '7, Very Cold (Duluth, MN)'),
		('8', '8, Subarctic (Fairbanks, AK)'),
		('Z1', 'CBECS - Zone 1'),
		('Z2', 'CBECS - Zone 2'),
		('Z3', 'CBECS - Zone 3'),
		('Z4', 'CBECS - Zone 4'),
		('Z5', 'CBECS - Zone 5')
		)

	site 		= models.ForeignKey(Site)
	zone 		= models.CharField(blank=False, max_length=100, choices=CLIMATE_ZONE)

	def __unicode__(self):
		return self.zone

class SiteType(models.Model):
	SITE_TYPE = (
		('Rural', 'Rural'),
		('Suburban', 'Suburban'),
		('Urban', 'Urban'),
		('Unknown', 'Unknown'))
	site 		= models.ForeignKey(Site)
	sitetype 	= models.CharField(max_length=8, choices=SITE_TYPE)

	def __unicode__(self):
		return self.type
