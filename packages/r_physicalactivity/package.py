# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhysicalactivity(RPackage):
	"""Process Accelerometer Data for Physical Activity Measurement

	It provides a function "wearingMarking" for classification of monitor
    wear and nonwear time intervals in accelerometer data collected to assess
    physical activity. The package also contains functions for making plot for 
    accelerometer data and obtaining the summary of various information including 
    daily monitor wear time and the mean monitor wear time during valid days.      
    "deliveryPred" and "markDelivery" can classify days for ActiGraph delivery by mail;
    "deliveryPreprocess" can process accelerometry data for analysis by zeropadding incomplete 
    days and removing low activity days; "markPAI" can categorize physical activity
    intensity level based on user-defined cut-points of accelerometer counts. It also
    supports importing ActiGraph AGD files with "readActigraph" and "queryActigraph" functions.
	"""
	
	cran = "PhysicalActivity" 

	version("0.2-4", md5="00fd495210ce274550393664c3773df2")

	depends_on("r@2.10:", type=("build", "run"))
