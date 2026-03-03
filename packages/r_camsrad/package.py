# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCamsrad(RPackage):
	"""Client for CAMS Radiation Service

	Copernicus Atmosphere Monitoring Service (CAMS) radiations service 
    provides time series of global, direct, and diffuse irradiations on horizontal
    surface, and direct irradiation on normal plane for the actual weather 
    conditions as well as for clear-sky conditions.
    The geographical coverage is the field-of-view of the Meteosat satellite,
    roughly speaking Europe, Africa, Atlantic Ocean, Middle East. The time coverage
    of data is from 2004-02-01 up to 2 days ago. Data are available with a time step
    ranging from 15 min to 1 month. For license terms and to create an account,
    please see <http://www.soda-pro.com/web-services/radiation/cams-radiation-service>. 
	"""
	
	homepage = "https://github.com/ropenscilabs/camsRad"
	cran = "camsRad" 

	version("0.3.0", md5="5bbcfb83a72080eb43e4d617b43c8507")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-httr@1.2.1:", type=("build", "run"))
	depends_on("r-xml2@1:", type=("build", "run"))
