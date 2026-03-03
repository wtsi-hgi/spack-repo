# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlumcarlo(RPackage):
	"""Monte-Carlo Methods for Simulating Luminescence Phenomena

	A collection of functions to simulate luminescence production in 
    dosimetric materials using Monte Carlo methods. Implemented are models for 
    delocalised transitions (e.g., Chen and McKeever (1997) <doi:10.1142/2781>), 
    localised transitions (e.g., Pagonis et al. (2019) <doi:10.1016/j.jlumin.2018.11.024>) 
    and tunnelling transitions (Jain et al. (2012) <doi:10.1088/0953-8984/24/38/385402> 
    and Pagonis et al. (2019) <doi:10.1016/j.jlumin.2018.11.024>). 
    Supported stimulation methods are thermal luminescence (TL), 
    continuous-wave optically stimulated luminescence (CW-OSL), 
    linearly-modulated optically stimulated luminescence (LM-OSL), 
    linearly-modulated infrared stimulated luminescence (LM-IRSL),
    and isothermal luminescence (ITL or ISO-TL).
	"""
	
	homepage = "https://CRAN.R-project.org/package=RLumCarlo"
	cran = "RLumCarlo" 

	version("0.1.9", md5="95de3cbf4ab97a30de3f802cf4a12dae")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-abind@1.4.5:", type=("build", "run"))
	depends_on("r-doparallel@1.0.17:", type=("build", "run"))
	depends_on("r-foreach@1.5.2:", type=("build", "run"))
	depends_on("r-khroma@1.9:", type=("build", "run"))
	depends_on("r-rcpp@1.0.9:", type=("build", "run"))
	depends_on("r-scatterplot3d@0.3:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.11.2:", type=("build", "run"))
