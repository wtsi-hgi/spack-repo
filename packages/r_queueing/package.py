# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQueueing(RPackage):
	"""Analysis of Queueing Networks and Models

	It provides versatile tools for analysis of birth and death based Markovian Queueing Models
    and Single and Multiclass Product-Form Queueing Networks.
    It implements M/M/1, M/M/c, M/M/Infinite, M/M/1/K, M/M/c/K, M/M/c/c, M/M/1/K/K, M/M/c/K/K, M/M/c/K/m, M/M/Infinite/K/K,
    Multiple Channel Open Jackson Networks, Multiple Channel Closed Jackson Networks,
    Single Channel Multiple Class Open Networks, Single Channel Multiple Class Closed Networks
    and Single Channel Multiple Class Mixed Networks.
    Also it provides a B-Erlang, C-Erlang and Engset calculators.
    This work is dedicated to the memory of D. Sixto Rios Insua.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "queueing" 

	version("0.2.12", md5="88c65cc3bfd68c2a461b3031bee8f1a2")

	depends_on("r@2.11.1:", type=("build", "run"))
