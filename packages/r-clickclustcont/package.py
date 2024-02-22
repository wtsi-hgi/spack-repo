# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClickclustcont(RPackage):
	"""Mixtures of Continuous Time Markov Models

	Provides an expectation maximization (EM) algorithm to fit a mixture of continuous time Markov models for use with clickstream or other sequence type data. Gallaugher, M.P.B and McNicholas, P.D. (2018) <arXiv:1802.04849>.
	"""
	
	cran = "ClickClustCont" 

	version("0.1.7", md5="b7462558f0a4492212d8e42c18a89af9")

	depends_on("r-gtools", type=("build", "run"))
