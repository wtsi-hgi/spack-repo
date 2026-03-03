# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROcsdata(RPackage):
	"""Download Data from the 'Open Case Studies' Repository

	
    Provides functions to access and download data from the 'Open Case Studies' <https://www.opencasestudies.org/> 
    repositories on 'GitHub' <https://github.com/opencasestudies>. Different functions enable 
    users to grab the data they need at different sections in the case study, as well as 
    download the whole case study repository. All the user needs to do is input the name of 
    the case study being worked on. The package relies on the httr::GET() function to access
    files through the 'GitHub' API. The functions usethis::use_zip() and usethis::create_from_github() 
    are used to clone and/or download the case study repositories. To cite an individual case study,
    please see the respective 'README' file at <https://github.com/opencasestudies/>.
    <https://github.com/opencasestudies/ocs-bp-rural-and-urban-obesity> 
    <https://github.com/opencasestudies/ocs-bp-air-pollution>
    <https://github.com/opencasestudies/ocs-bp-vaping-case-study>
    <https://github.com/opencasestudies/ocs-bp-opioid-rural-urban>
    <https://github.com/opencasestudies/ocs-bp-RTC-wrangling>
    <https://github.com/opencasestudies/ocs-bp-RTC-analysis>
    <https://github.com/opencasestudies/ocs-bp-youth-disconnection>
    <https://github.com/opencasestudies/ocs-bp-youth-mental-health>
    <https://github.com/opencasestudies/ocs-bp-school-shootings-dashboard>
    <https://github.com/opencasestudies/ocs-bp-co2-emissions>
    <https://github.com/opencasestudies/ocs-bp-diet>.
	"""
	
	homepage = "https://github.com/opencasestudies/OCSdata"
	cran = "OCSdata" 

	version("1.0.2", md5="97af8ff3ef00185fc139e4f45c806eca")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-usethis@2:", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-httr@1.4:", type=("build", "run"))
