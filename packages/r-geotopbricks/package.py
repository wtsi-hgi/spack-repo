# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeotopbricks(RPackage):
	"""An R Plug-in for the Distributed Hydrological Model GEOtop

	It analyzes raster maps and other information as input/output
    files from the Hydrological Distributed Model GEOtop. It contains functions
    and methods to import maps and other keywords from geotop.inpts file. Some
    examples with simulation cases of GEOtop 2.x/3.x are presented in the package.
    Any information about the GEOtop Distributed Hydrological Model source code
    is available on www.geotop.org. Technical details about the model are
    available in Endrizzi et al (2014) <https://gmd.copernicus.org/articles/7/2831/2014/gmd-7-2831-2014.html>.
	"""
	
	homepage = "https://zenodo.org/record/8228413"
	cran = "geotopbricks" 

	version("1.5.8.0", md5="9e854fe21d04ddec678735af0cc14150")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
