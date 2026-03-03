# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdetect(RPackage):
	"""Isolate-Detect Methodology for Multiple Change-Point Detection

	Provides efficient implementation of the Isolate-Detect
    methodology for the consistent estimation of the number and location of multiple 
    change-points in one-dimensional data sequences from the "deterministic 
    + noise" model. For details on the Isolate-Detect methodology, please see Anastasiou and
    Fryzlewicz (2018) <https://docs.wixstatic.com/ugd/24cdcc_6a0866c574654163b8255e272bc0001b.pdf>.
    Currently implemented scenarios are: piecewise-constant signal with Gaussian
    noise, piecewise-constant signal with heavy-tailed noise, continuous piecewise-linear 
    signal with Gaussian noise, continuous piecewise-linear signal with heavy-tailed noise.
	"""
	
	cran = "IDetect" 

	version("0.1.0", md5="081cb2a1e40d7f8bf28c94519bc4c3a9")

	depends_on("r@3.3:", type=("build", "run"))
