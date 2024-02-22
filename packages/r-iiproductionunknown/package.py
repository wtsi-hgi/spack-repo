# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIiproductionunknown(RPackage):
	"""Analyzing Data Through of Percentage of Importance Indice
(Production Unknown) and Its Derivations

	The Importance Index (I.I.) can determine the loss and solution sources for a system in certain knowledge areas (e.g., agronomy), when production (e.g., fruits) is known (Demolin-Leite, 2021). Events (e.g., agricultural pest) can have different magnitudes (numerical measurements), frequencies, and distributions (aggregate, random, or regular) of event occurrence, and I.I. bases in this triplet (Demolin-Leite, 2021) <https://cjascience.com/index.php/CJAS/article/view/1009/1319>. Usually, the higher the magnitude and frequency of aggregated distribution, the greater the problem or the solution (e.g., natural enemies versus pests) for the system (Demolin-Leite, 2021). However, the final production of the system is not always known or is difficult to determine (e.g., degraded area recovery). A derivation of the I.I. is the percentage of Importance Index-Production Unknown (% I.I.-PU) that can detect the loss or solution sources, when production is unknown for the system (Demolin-Leite, 2024) <DOI:10.1590/1519-6984.253218>. 
	"""
	
	cran = "IIProductionUnknown" 

	version("0.0.3", md5="bcc72308aee3a0a790041a407ef84c66")

	depends_on("r-crayon", type=("build", "run"))
