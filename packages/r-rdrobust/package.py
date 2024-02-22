# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdrobust(RPackage):
	"""Robust Data-Driven Statistical Inference in
Regression-Discontinuity Designs

	Regression-discontinuity (RD) designs are quasi-experimental research designs popular in social, behavioral and natural sciences. The RD design is usually employed to study the (local) causal effect of a treatment, intervention or policy. This package provides tools for data-driven graphical and analytical statistical inference in RD	designs: rdrobust() to construct local-polynomial point estimators and robust confidence intervals for average treatment effects at the 	cutoff in Sharp, Fuzzy and Kink RD settings, rdbwselect() to perform bandwidth selection for the different procedures implemented, and rdplot() to conduct exploratory data analysis (RD plots).
	"""
	
	cran = "rdrobust" 

	version("2.2", md5="4511d673066603d12c7d52b4162a7b4b")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
