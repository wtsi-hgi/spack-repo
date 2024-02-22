# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhpcblasctl(RPackage):
	"""Control the Number of Threads on 'BLAS'

	Control the number of threads on 'BLAS' (Aka 'GotoBLAS', 'OpenBLAS', 'ACML', 'BLIS' and 'MKL').
  And possible to control the number of threads in 'OpenMP'.
  Get a number of logical cores and physical cores if feasible.
	"""
	
	homepage = "https://prs.ism.ac.jp/~nakama/Rhpc/"
	cran = "RhpcBLASctl" 

	version("0.23-42", md5="825ec304404cad180a6bfb5aef5204b7")

