# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVariablescreening(RPackage):
	"""High-Dimensional Screening for Semiparametric Longitudinal
Regression

	Implements variable screening techniques for ultra-high
    dimensional regression settings.  Techniques for independent (iid) data,
    varying-coefficient models, and longitudinal data are implemented. The package
     currently contains three screen functions: screenIID(), screenLD() and screenVCM(),
     and six methods for simulating dataset: simulateDCSIS(), simulateLD, simulateMVSIS(),
     simulateMVSISNY(), simulateSIRS() and simulateVCM(). The package is based on the work of
    Li-Ping ZHU, Lexin LI, Runze LI, and Li-Xing ZHU (2011) <DOI:10.1198/jasa.2011.tm10563>,
    Runze LI, Wei ZHONG, & Liping ZHU (2012) <DOI:10.1080/01621459.2012.695654>,
    Jingyuan LIU, Runze LI, & Rongling WU (2014) <DOI:10.1080/01621459.2013.850086>
    Hengjian CUI, Runze LI, & Wei ZHONG (2015) <DOI:10.1080/01621459.2014.920256>, and
    Wanghuan CHU, Runze LI and Matthew REIMHERR (2016) <DOI:10.1214/16-AOAS912>.
	"""
	
	cran = "VariableScreening" 

	version("0.2.1", md5="6ecbf73f0e8a3ea2fd7322bf097122ea")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-gee", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
