# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHomnormal(RPackage):
	"""Tests of Homogeneity of Variances

	Most common exact, asymptotic and resample based tests are provided for testing the 
            homogeneity of variances of k normal distributions under normality. 
            These tests are Barlett, Bhandary & Dai, Brown & Forsythe, Chang et al., Gokpinar & Gokpinar, Levene, Liu and Xu, Gokpinar. 
            Also, a data generation function from multiple normal distribution is provided using any multiple normal parameters.  
            Bartlett, M. S. (1937) <doi:10.1098/rspa.1937.0109> 
            Bhandary, M., & Dai, H. (2008) <doi:10.1080/03610910802431011>
            Brown, M. B., & Forsythe, A. B. (1974).<doi:10.1080/01621459.1974.10482955>
            Chang, C. H., Pal, N., & Lin, J. J. (2017) <doi:10.1080/03610918.2016.1202277>
            Gokpinar E. & Gokpinar F. (2017) <doi:10.1080/03610918.2014.955110>
            Liu, X., & Xu, X. (2010) <doi:10.1016/j.spl.2010.05.017>
            Levene, H. (1960) <https://cir.nii.ac.jp/crid/1573950400526848896>
            Gökpınar, E. (2020) <doi:10.1080/03610918.2020.1800037>.
	"""
	
	cran = "homnormal" 

	version("0.1", md5="0bccc663a8034f85a5a42176977924b1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-huxtable@5.4:", type=("build", "run"))
