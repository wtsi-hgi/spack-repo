# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGllm(RPackage):
	"""Generalised log-Linear Model

	Routines for log-linear models of incomplete contingency tables,
             including some latent class models, via EM and Fisher scoring
             approaches. Allows bootstrapping. See Espeland and Hui (1987)
             <doi:10.2307/2531553> for general approach.
	"""
	
	homepage = "https://genepi.qimr.edu.au/Staff/davidD/#loglin"
	cran = "gllm" 

	version("0.38", md5="b23a312cd7aa18c3086d5e4f038c5db3")

	depends_on("r@0.99:", type=("build", "run"))
