# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNnr(RPackage):
	"""Neural Networks Made Algebraic

	Do algebraic operations on neural networks. We seek here to implement
  in R, operations on neural networks and their resulting approximations. Our operations derive
  their descriptions mainly from
  Rafi S., Padgett, J.L., and Nakarmi, U. (2024), "Towards an Algebraic Framework For Approximating Functions Using Neural Network Polynomials", <doi:10.48550/arXiv.2402.01058>, 
  Grohs P., Hornung, F., Jentzen, A. et al. (2023), "Space-time error estimates for deep neural network approximations for differential equations", <doi:10.1007/s10444-022-09970-2>,
  Jentzen A., Kuckuck B., von Wurstemberger, P. (2023), "Mathematical Introduction to Deep Learning Methods, Implementations, and Theory" <doi:10.48550/arXiv.2310.20360>.
  Our implementation is meant mainly as a pedagogical tool, and proof of concept. Faster implementations with 
  deeper vectorizations may be made in future versions. 
	"""
	
	homepage = "https://github.com/2shakilrafi/nnR/"
	cran = "nnR" 

	version("0.1.0", md5="c72b3ddcf562b91a075c27128720570e")

	depends_on("r@4.1:", type=("build", "run"))
