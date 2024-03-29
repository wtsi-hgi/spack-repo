# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmmixmfa(RPackage):
	"""Mixture Models with Component-Wise Factor Analyzers

	We provide functions to fit finite mixtures of multivariate normal or t-distributions to 
    data with various factor analytic structures adopted for the covariance/scale matrices. The 
    factor analytic structures available include mixtures of factor analyzers and mixtures of common 
    factor analyzers. The latter approach is so termed because the matrix of factor loadings is
    common to components before the component-specific rotation of the component factors to 
    make them white noise. Note that the component-factor loadings are not common after 
    this rotation. Maximum likelihood estimators of model parameters are obtained via the 
    Expectation-Maximization algorithm. See descriptions of the algorithms used in
    McLachlan GJ, Peel D (2000) <doi:10.1002/0471721182.ch8>
    McLachlan GJ, Peel D (2000) <ISBN:1-55860-707-2> 
    McLachlan GJ, Peel D, Bean RW (2003) <doi:10.1016/S0167-9473(02)00183-4> 
    McLachlan GJ, Bean RW, Ben-Tovim Jones L (2007) <doi:10.1016/j.csda.2006.09.015> 
    Baek J, McLachlan GJ, Flack LK (2010) <doi:10.1109/TPAMI.2009.149> 
    Baek J, McLachlan GJ (2011) <doi:10.1093/bioinformatics/btr112> 
    McLachlan GJ, Baek J, Rathnayake SI (2011) <doi:10.1002/9781119995678.ch9>.
	"""
	
	homepage = "https://github.com/suren-rathnayake/EMMIXmfa"
	cran = "EMMIXmfa" 

	version("2.0.14", md5="58cccb97855729864c2b74be475ed848")

