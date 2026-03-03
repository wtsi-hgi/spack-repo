# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcorvs(RPackage):
	"""Variable Selection Algorithms Using the Distance Correlation

	The 'FBED' and 'mmpc' variable selection algorithms have been implemented using the distance correlation. The references include: Tsamardinos I., Aliferis C. F. and Statnikov A. (2003). "Time and sample efficient discovery of Markovblankets and direct causal relations". In Proceedings of the ninth ACM SIGKDD international Conference. <doi:10.1145/956750.956838>. Borboudakis G. and Tsamardinos I. (2019). "Forward-backward selection with early dropping". Journal of Machine Learning Research, 20(8): 1--39. <doi:10.48550/arXiv.1705.10770>. Huo X. and Szekely G.J. (2016). "Fast computing for distance covariance". Technometrics, 58(4): 435--447. <doi:10.1080/00401706.2015.1054435>.
	"""
	
	cran = "dcorVS" 

	version("1.0", md5="a1065d18ef8c3f96144a5677d70112c1")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dcov", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
