# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlurmr(RPackage):
	"""A Lightweight Wrapper for 'Slurm'

	'Slurm', Simple Linux Utility for Resource Management
          <https://slurm.schedmd.com/>, is a popular 'Linux' based software used to 
          schedule jobs in 'HPC' (High Performance Computing) clusters. This R package
          provides a specialized lightweight wrapper of 'Slurm' with a syntax similar to
          that found in the 'parallel' R package. The package also includes a method for
          creating socket cluster objects spanning multiple nodes that can be used with
          the 'parallel' package.
	"""
	
	homepage = "https://github.com/USCbiostats/slurmR"
	cran = "slurmR" 

	version("0.5-4", md5="731433b070b0f6d3287bcc8c762d4c41")

	depends_on("r@3.3:", type=("build", "run"))
