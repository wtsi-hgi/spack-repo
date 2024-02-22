# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvcurve(RPackage):
	"""Plots Survival Curves Element by Element

	Plots survival models from the 'survival' package. Additionally, it
    plots curves of multistate models from the 'mstate' package. Typically, a
    plot is drawn by the sequence survplot(), confIntArea(), survCurve() and
    nrAtRisk(). The separation of the plot in this 4 functions allows for great
    flexibility to make a custom plot for publication.
	"""
	
	cran = "survCurve" 

	version("1.0", md5="38eeabb4dc11ac1657845dcc95a2769e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-survival@3.1:", type=("build", "run"))
