# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBacistool(RPackage):
	"""Bayesian Classification and Information Sharing (BaCIS) Tool for
the Design of Multi-Group Phase II Clinical Trials

	Provides the design of multi-group phase
    II clinical trials with binary outcomes using the hierarchical Bayesian
    classification and information sharing (BaCIS) model. Subgroups are classified
    into two clusters on the basis of their outcomes mimicking the hypothesis
    testing framework. Subsequently, information sharing takes place within
    subgroups in the same cluster, rather than across all subgroups. This method can
    be applied to the design and analysis of multi-group clinical trials with binary
    outcomes. Reference: Nan Chen and J. Jack Lee (2019) <doi:10.1002/bimj.201700275>.
	"""
	
	cran = "bacistool" 

	version("1.0.0", md5="1e2ac7a2eeb6bb6b89716c4537930eee")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("jags@4.3.0:", type=("build", "link", "run"))
