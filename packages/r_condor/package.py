# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCondor(RPackage):
	"""Interact with 'Condor' from R via SSH

	Interact with 'Condor' from R via SSH connection. Files are first
  uploaded from user machine to submitter machine, and the job is then submitted
  from the submitter machine to 'Condor'. Functions are provided to submit,
  list, and download 'Condor' jobs from R. 'Condor' is an open source
  high-throughput computing software framework for distributed parallelization
  of computationally intensive tasks.
	"""
	
	homepage = "https://github.com/PacificCommunity/ofp-sam-condor"
	cran = "condor" 

	version("2.1.0", md5="8763431ba9220060e797ef75c3a49b7a")

	depends_on("r-ssh", type=("build", "run"))
