# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJscore(RPackage):
	"""Calculates the j-Score Between Two Clustering Assignments

	The jscore() function in the package calculates the J-Score metric between two clustering
    assignments. The score is designed to address some problems with existing common metrics such 
    as problem of matching. The details of J-score is described in Ahmadinejad and Liu. (2021) <arXiv:2109.01306>.
	"""
	
	homepage = "https://github.com/liliulab/jscore"
	cran = "jScore" 

	version("0.1.0", md5="15d2fab10a2e20e85b8b1ec6201bce88")

