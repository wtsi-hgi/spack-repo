# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwarmverse(RPackage):
	"""Swarm Space Creation

	Provides a pipeline for the comparative analysis of 
  collective movement data (e.g. fish schools, bird flocks, baboon troops) by 
  processing 2-dimensional positional data (x,y,t) from GPS trackers or computer
  vision tracking systems, discretizing events of collective motion, calculating
  a set of established metrics that characterize each event, and placing the
  events in a multi-dimensional swarm space constructed from these metrics.
  The swarm space concept, the metrics and data sets included are described in:
  Papadopoulou Marina, Furtbauer Ines, O'Bryan Lisa R., Garnier Simon, 
  Georgopoulou Dimitra G., Bracken Anna M., Christensen Charlotte and King
  Andrew J. (2023) <doi:10.1098/rstb.2022.0068>.
	"""
	
	homepage = "https://marinapapa.github.io/swaRmverse/"
	cran = "swaRmverse" 

	version("0.1.0", md5="724ab46980870af675b57849b5f9a834")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-trackdf", type=("build", "run"))
	depends_on("r-swarm", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
