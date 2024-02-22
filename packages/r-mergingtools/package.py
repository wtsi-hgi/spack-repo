# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMergingtools(RPackage):
	"""Tools to Merge Hardware Event Monitors (HEMs) Coming from
Separate Subexperiments into One Single Dataframe

	Implementation of two tools to merge Hardware Event Monitors (HEMs) from different subexperiments. Hardware Reading and Merging (HRM), which uses order statistics to merge; and MUlti-Correlation HEM (MUCH) which merges using a multivariate normal distribution. The reference paper for HRM is: S. Vilardell, I. Serra, R. Santalla, E. Mezzetti, J. Abella and F. J. Cazorla, "HRM: Merging Hardware Event Monitors for Improved Timing Analysis of Complex MPSoCs," in IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, vol. 39, no. 11, pp. 3662-3673, Nov. 2020, <doi:10.1109/TCAD.2020.3013051>. For MUCH: S. Vilardell, I. Serra, E. Mezzetti, J. Abella, and F. J. Cazorla. 2021. "MUCH: exploiting pairwise hardware event monitor correlations for improved timing analysis of complex MPSoCs". In Proceedings of the 36th Annual ACM Symposium on Applied Computing (SAC '21). Association for Computing Machinery. <doi:10.1145/3412841.3441931>. This work has been supported by the European Research Council (ERC) under the European Union's Horizon 2020 research and innovation programme (grant agreement No. 772773).
	"""
	
	cran = "mergingTools" 

	version("1.0.1", md5="5f1423c1f86231df1f41a2f67b0d64e7")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
