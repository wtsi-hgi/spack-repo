# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RControlfunctioniv(RPackage):
	"""Control Function Methods with Possibly Invalid Instrumental
Variables

	Inference with control function methods for nonlinear outcome models when the model is known ('Guo and Small' (2016) <arXiv:1602.01051>) and when unknown but semiparametric ('Li and Guo' (2021) <arXiv:2010.09922>).
	"""
	
	homepage = "https://github.com/zijguo/controlfunctionIV"
	cran = "controlfunctionIV" 

	version("0.1.1", md5="0ae342564a16e6355d67b2219d374ed9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dr", type=("build", "run"))
	depends_on("r-orthodr", type=("build", "run"))
	depends_on("r-aer", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
