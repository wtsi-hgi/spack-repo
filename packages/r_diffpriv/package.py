# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffpriv(RPackage):
	"""Easy Differential Privacy

	An implementation of major general-purpose mechanisms for privatizing
    statistics, models, and machine learners, within the framework of differential
    privacy of Dwork et al. (2006) <doi:10.1007/11681878_14>. Example mechanisms
    include the Laplace mechanism for releasing numeric aggregates, and the 
    exponential mechanism for releasing set elements. A sensitivity sampler 
    (Rubinstein & Alda, 2017) <arXiv:1706.02562> permits sampling target 
    non-private function sensitivity; combined with the generic mechanisms, it 
    permits turn-key privatization of arbitrary programs.
	"""
	
	homepage = "https://github.com/brubinstein/diffpriv"
	cran = "diffpriv" 

	version("0.4.2", md5="2dd954cda8193867eb2fde2d34db4537")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
