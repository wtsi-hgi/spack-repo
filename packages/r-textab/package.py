# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTextab(RPackage):
	"""Create Highly-Customized 'LaTeX' Tables

	Generate 'LaTeX' tables directly from R. It builds 'LaTeX' tables in blocks in the spirit of 'ggplot2' using the '+' and '/' operators for concatenation in the vertical and horizontal dimensions, respectively. It exports tables in the 'LaTeX' tabular environment using '.tex' code. It can compile '.tex' code to 'PDF' automatically.
	"""
	
	homepage = "https://setzler.github.io/textab/"
	cran = "textab" 

	version("1.0.1", md5="662ab524116838bf2276859a963ea3af")

