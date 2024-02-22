# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlamingos(RPackage):
	"""Functional Latent Data Models for Clustering Heterogeneous
Curves ('FLaMingos')

	Provides a variety of original and flexible user-friendly 
    statistical latent variable models for the simultaneous clustering and 
    segmentation of heterogeneous functional data (i.e time series, or more 
    generally longitudinal data, fitted by unsupervised algorithms, including 
    EM algorithms. Functional Latent Data Models for Clustering heterogeneous 
    curves ('FLaMingos') are originally introduced and written in 'Matlab' by
    Faicel Chamroukhi 
    <https://github.com/fchamroukhi?utf8=?&tab=repositories&q=mix&type=public&language=matlab>. 
    The references are mainly the following ones.
    Chamroukhi F. (2010) <https://chamroukhi.com/FChamroukhi-PhD.pdf>.
    Chamroukhi F., Same A., Govaert, G. and Aknin P. (2010) <doi:10.1016/j.neucom.2009.12.023>.
    Chamroukhi F., Same A., Aknin P. and Govaert G. (2011). <doi:10.1109/IJCNN.2011.6033590>.
    Same A., Chamroukhi F., Govaert G. and Aknin, P. (2011) <doi:10.1007/s11634-011-0096-5>.
    Chamroukhi F., and Glotin H. (2012) <doi:10.1109/IJCNN.2012.6252818>.
    Chamroukhi F., Glotin H. and Same A. (2013) <doi:10.1016/j.neucom.2012.10.030>.
    Chamroukhi F. (2015) <https://chamroukhi.com/FChamroukhi-HDR.pdf>.
    Chamroukhi F. and Nguyen H-D. (2019) <doi:10.1002/widm.1298>.
	"""
	
	homepage = "https://github.com/fchamroukhi/FLaMingos"
	cran = "flamingos" 

	version("0.1.0", md5="ce46e73db071285f46b6316c1ec995e8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
