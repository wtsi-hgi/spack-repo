# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAromaAffymetrix(RPackage):
	"""Analysis of Large Affymetrix Microarray Data Sets

	A cross-platform R framework that facilitates processing of any number of Affymetrix microarray samples regardless of computer system.  The only parameter that limits the number of chips that can be processed is the amount of available disk space.  The Aroma Framework has successfully been used in studies to process tens of thousands of arrays.  This package has actively been used since 2006.
	"""
	
	homepage = "https://www.aroma-project.org/"
	cran = "aroma.affymetrix" 

	version("3.2.2", md5="2823c97ceedc1ee510ffad76f6a84e96")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-r-utils@2.9:", type=("build", "run"))
	depends_on("r-aroma-core@3.2:", type=("build", "run"))
	depends_on("r-r-methodss3@1.7.1:", type=("build", "run"))
	depends_on("r-r-oo@1.23:", type=("build", "run"))
	depends_on("r-r-cache@0.14:", type=("build", "run"))
	depends_on("r-r-devices@2.16.1:", type=("build", "run"))
	depends_on("r-r-filesets@2.13:", type=("build", "run"))
	depends_on("r-aroma-apd@0.6:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixstats@0.55:", type=("build", "run"))
	depends_on("r-listenv", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
