# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReplicationsuccess(RPackage):
	"""Design and Analysis of Replication Studies

	Provides utilities for the design and analysis of replication
    studies.  Features both traditional methods based on statistical
    significance and more recent methods such as the sceptical p-value;
    Held L. (2020) <doi:10.1111/rssa.12493>, Held et al. (2022)
    <doi:10.1214/21-AOAS1502>, Micheloud et al. (2023) <doi:10.1111/stan.12312>.
    Also provides related methods including the harmonic mean chi-squared
    test; Held, L. (2020) <doi:10.1111/rssc.12410>, and intrinsic
    credibility; Held, L. (2019) <doi:10.1098/rsos.181534>. Contains
    datasets from five large-scale replication projects.
	"""
	
	homepage = "https://crsuzh.github.io/ReplicationSuccess/"
	cran = "ReplicationSuccess" 

	version("1.3.2", md5="c9b398f89cf018f42ba8241f7a7934f3")
	version("1.3.1", md5="368184030ed0a1bdafd37958fd7130e0")

