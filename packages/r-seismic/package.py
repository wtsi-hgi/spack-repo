# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeismic(RPackage):
	"""Predict Information Cascade by Self-Exciting Point Process

	An implementation of self-exciting point process model for information cascades, which occurs when many people engage in the same acts after observing the actions of others (e.g. post resharings on Facebook or Twitter). It provides functions to estimate the infectiousness of an information cascade and predict its popularity given the observed history. See <http://snap.stanford.edu/seismic/> for more information and datasets.
	"""
	
	homepage = "http://snap.stanford.edu/seismic/"
	cran = "seismic" 

	version("1.1", md5="d35446a648617db2f720f51124adaeb7")

