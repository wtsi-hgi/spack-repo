# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdplot(RPackage):
	"""Visualising Molecular Dynamics Analyses

	Provides automatization for plot generation succeeding common molecular dynamics analyses.
             This includes straightforward plots, such as RMSD (Root-Mean-Square-Deviation) and
             RMSF (Root-Mean-Square-Fluctuation) but also more sophisticated ones such as
             dihedral angle maps, hydrogen bonds, cluster bar plots and
             DSSP (Definition of Secondary Structure of Proteins) analysis. Currently able to load
             GROMOS, GROMACS and AMBER formats, respectively.
	"""
	
	homepage = "https://github.com/MDplot/MDplot"
	cran = "MDplot" 

	version("1.0.1", md5="5ff2dd52ec57a8e9ffd023c92db63fb5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
