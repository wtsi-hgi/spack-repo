# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpdynmod(RPackage):
	"""Spatio-Dynamic Wetland Plant Communities Model

	A spatio-dynamic modelling package that focuses on three
    characteristic wetland plant communities in a semiarid Mediterranean
    wetland in response to hydrological pressures from the catchment. The
    package includes the data on watershed hydrological pressure and the
    initial raster maps of plant communities but also allows for random initial
    distribution of plant communities. For more detailed info see: Martinez-Lopez et al. (2015) <doi:10.1016/j.ecolmodel.2014.11.024>.
	"""
	
	homepage = "https://github.com/javimarlop/spdynmod"
	cran = "spdynmod" 

	version("1.1.6", md5="7e867beee5524bff647a39979de595fc")

	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-animation", type=("build", "run"))
