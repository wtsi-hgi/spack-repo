# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAromaCore(RPackage):
	"""Core Methods and Classes Used by 'aroma.*' Packages Part of the
Aroma Framework

	Core methods and classes used by higher-level 'aroma.*' packages
        part of the Aroma Project, e.g. 'aroma.affymetrix' and 'aroma.cn'.
	"""
	
	homepage = "https://github.com/HenrikBengtsson/aroma.core"
	cran = "aroma.core" 

	version("3.3.1", md5="08a9464242f05874971c351aef3db773")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-r-utils@2.10.1:", type=("build", "run"))
	depends_on("r-r-filesets@2.14:", type=("build", "run"))
	depends_on("r-r-devices@2.16.1:", type=("build", "run"))
	depends_on("r-r-methodss3@1.8.1:", type=("build", "run"))
	depends_on("r-r-oo@1.24:", type=("build", "run"))
	depends_on("r-r-cache@0.14:", type=("build", "run"))
	depends_on("r-r-rsp@0.44:", type=("build", "run"))
	depends_on("r-matrixstats@0.57:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-pscbs@0.65:", type=("build", "run"))
	depends_on("r-listenv", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
