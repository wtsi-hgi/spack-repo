# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJointdiag(RPackage):
	"""Joint Approximate Diagonalization of a Set of Square Matrices

	Different algorithms to perform approximate joint diagonalization
	of a finite set of square matrices. Depending on the algorithm,
	orthogonal or non-orthogonal diagonalizer is found. These algorithms
	are particularly useful in the context of blind source separation. 
	Original publications of the algorithms can be found in 
	Ziehe et al. (2004), Pham and Cardoso (2001) <doi:10.1109/78.942614>, 
	Souloumiac (2009) <doi:10.1109/TSP.2009.2016997>, 
	Vollgraff and Obermayer <doi:10.1109/TSP.2006.877673>. An example of 
	application in the context of Brain-Computer Interfaces EEG denoising
	can be found in Gouy-Pailler et al (2010) <doi:10.1109/TBME.2009.2032162>.
	"""
	
	homepage = "https://github.com/gouypailler/jointDiag"
	cran = "jointDiag" 

	version("0.4", md5="c29195201c6652ce051141fbbd2d37d1")

