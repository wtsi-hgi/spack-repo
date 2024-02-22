# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REarthdatalogin(RPackage):
	"""NASA 'EarthData' Login Utilities

	Providing easy, portable access to NASA 'EarthData' products
  through the use of bearer tokens. Much of NASA's public data catalogs hosted
  and maintained by its 12 Distributed Active Archive Centers ('DAACs') are
  now made available on the Amazon Web Services 'S3' storage.  However, 
  accessing this data through the standard 'S3' API is restricted to only to 
  compute resources running inside 'us-west-2' Data Center in Portland, Oregon,
  which allows NASA to avoid being charged data egress rates. This package
  provides public access to the data from any networked device by using the 
  'EarthData' login application programming interface (API),
  <https://www.earthdata.nasa.gov/eosdis/science-system-description/eosdis-components/earthdata-login>,
  providing convenient authentication and access to cloud-hosted NASA 'EarthData'
  products. This makes access to a wide range of earth observation data from 
  any location straight forward and compatible with R packages that are 
  widely used with cloud native earth observation data (such as 'terra',
  'sf', etc.)
	"""
	
	homepage = "https://boettiger-lab.github.io/earthdatalogin/"
	cran = "earthdatalogin" 

	version("0.0.2", md5="20fd7a97571a90ea7e05ba2937e3086d")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
