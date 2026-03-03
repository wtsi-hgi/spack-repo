# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnn(RPackage):
	"""Recurrent Neural Network

	Implementation of a Recurrent Neural Network architectures in native R, including Long Short-Term Memory (Hochreiter and Schmidhuber, <doi:10.1162/neco.1997.9.8.1735>), Gated Recurrent Unit (Chung et al., <arXiv:1412.3555>) and vanilla RNN.
	"""
	
	homepage = "https://qua.st/rnn/"
	cran = "rnn" 

	version("1.9.0", md5="d46e03d1e9c44bb4f51e576ad145e5c0")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-attention", type=("build", "run"))
	depends_on("r-sigmoid@1.4:", type=("build", "run"))
