# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStats19(RPackage):
	"""Work with Open Road Traffic Casualty Data from Great Britain

	Tools to help download, process and analyse the UK road collision data collected using the
  'STATS19' form. The datasets are provided as 'CSV' files with detailed road safety information about the
  circumstances of car crashes and other incidents on the roads resulting in casualties in Great Britain
  from 1979 to present. Tables are available on 'colissions' with the circumstances (e.g. speed limit
  of road), information about  'vehicles' involved (e.g. type of vehicle), and 'casualties' (e.g. age).
  The statistics relate only to events on public roads that were reported
  to the police, and subsequently recorded, using the 'STATS19' collision reporting form. See
  the Department for Transport website 
  <https://www.data.gov.uk/dataset/cb7ae6f0-4be6-4935-9277-47e5ce24a11f/road-safety-data> for more
  information on these datasets.
  The package is described in a paper in the Journal of Open Source Software
  (Lovelace et al. 2019) <doi:10.21105/joss.01181>.
  See 
  Gilardi et al. (2022) <doi:10.1111/rssa.12823>,
  Vidal-Tortosa et al. (2021) <doi:10.1016/j.jth.2021.101291>, and
  Tait et al. (2023) <doi:10.1016/j.aap.2022.106895> for examples of how the data can be used for
  methodological and empirical road safety research.
	"""
	
	homepage = "https://github.com/ropensci/stats19"
	cran = "stats19" 

	version("3.0.3", md5="bd443eda5d14f3de679cdca167140f56", url="https://cran.r-project.org/src/contrib/stats19_3.0.3.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
