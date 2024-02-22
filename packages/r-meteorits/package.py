# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeteorits(RPackage):
	"""Mixture-of-Experts Modeling for Complex Non-Normal Distributions

	Provides a unified mixture-of-experts (ME) modeling and 
    estimation framework with several original and flexible ME models to 
    model, cluster and classify heterogeneous data in many complex 
    situations where the data are distributed according to non-normal, 
    possibly skewed distributions, and when they might be corrupted by 
    atypical observations. Mixtures-of-Experts models for complex and 
    non-normal distributions ('meteorits') are originally introduced and 
    written in 'Matlab' by Faicel Chamroukhi. The references are mainly the 
    following ones. The references are mainly the following ones.
    Chamroukhi F., Same A., Govaert, G. and Aknin P. (2009) <doi:10.1016/j.neunet.2009.06.040>.
    Chamroukhi F. (2010) <https://chamroukhi.com/FChamroukhi-PhD.pdf>.
    Chamroukhi F. (2015) <arXiv:1506.06707>.
    Chamroukhi F. (2015) <https://chamroukhi.com/FChamroukhi-HDR.pdf>.
    Chamroukhi F. (2016) <doi:10.1109/IJCNN.2016.7727580>.
    Chamroukhi F. (2016) <doi:10.1016/j.neunet.2016.03.002>.
    Chamroukhi F. (2017) <doi:10.1016/j.neucom.2017.05.044>.
	"""
	
	homepage = "https://github.com/fchamroukhi/MEteorits"
	cran = "meteorits" 

	version("0.1.1", md5="59d2ec5361d28897424ea1b35fdd959b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
