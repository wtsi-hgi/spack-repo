# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTlrmvnmvt(RPackage):
	"""Low-Rank Methods for MVN and MVT Probabilities

	Implementation of the classic Genz algorithm and a novel tile-low-rank algorithm for computing	relatively high-dimensional multivariate normal (MVN) and Student-t (MVT) probabilities. 
	References used for this package:
	Foley, James, Andries van Dam, Steven Feiner, and John Hughes. 
	"Computer Graphics: Principle and Practice". Addison-Wesley 
	Publishing Company. Reading, Massachusetts (1987, ISBN:0-201-84840-6 1);
	Genz, A., "Numerical computation of multivariate
	normal probabilities," Journal of Computational and
	Graphical Statistics, 1, 141-149 (1992) <doi:10.1080/10618600.1992.10477010>;
    Cao, J., Genton, M. G., Keyes, D. E., & Turkiyyah, G. M. "Exploiting Low
    Rank Covariance Structures for Computing High-Dimensional Normal and Student-
    t Probabilities," Statistics and Computing, 31.1, 1-16 (2021) 
    <doi:10.1007/s11222-020-09978-y>;
    Cao, J., Genton, M. G., Keyes, D. E., & Turkiyyah, G. M. "tlrmvnmvt: 
    Computing High-Dimensional Multivariate Normal and Student-t Probabilities 
    with Low-Rank Methods in R," Journal of Statistical Software, 101.4, 
    1-25 (2022) <doi:10.18637/jss.v101.i04>.
	"""
	
	cran = "tlrmvnmvt" 

	version("1.1.2", md5="fcca5e0340fd39c3686d59cd9ae10fb2")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcpp@1.0.8:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.5:", type=("build", "run"))
	depends_on("r-bh@1.69.0.1:", type=("build", "run"))
