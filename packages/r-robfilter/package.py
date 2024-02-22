# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobfilter(RPackage):
	"""Robust Time Series Filters

	Implementations for several robust procedures that allow for (online)
        extraction of the signal of univariate or multivariate time series by
        applying robust regression techniques to a moving time window are provided.
        Included are univariate filtering procedures based on repeated-median 
        regression as well as hybrid and trimmed filters derived from it; 
        see Schettlinger et al. (2006) <doi:10.1515/BMT.2006.010>. The adaptive 
        online repeated median by Schettlinger et al. (2010) <doi:10.1002/acs.1105> 
        and the slope comparing adaptive repeated median by Borowski and Fried (2013) 
        <doi:10.1007/s11222-013-9391-7> choose the width of the moving time 
        window adaptively. Multivariate versions are also provided; see  
        Borowski et al. (2009) <doi:10.1080/03610910802514972> for a multivariate 
        online adaptive repeated median and Borowski (2012) <doi:10.17877/DE290R-14393>  
        for a multivariate slope comparing adaptive repeated median. Furthermore, 
        a repeated-median based filter with automatic outlier replacement and 
        shift detection is provided; see Fried (2004) <doi:10.1080/10485250410001656444>.
	"""
	
	homepage = "https://msnat.statistik.tu-dortmund.de/en/team/chair/"
	cran = "robfilter" 

	version("4.1.4", md5="2195de161db6a740067f1fff71b9fab2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
