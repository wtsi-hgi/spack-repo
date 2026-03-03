# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmacofx(RPackage):
	"""Flexible Multidimensional Scaling and 'smacof' Extensions

	Flexible multidimensional scaling (MDS) methods centered around scaling with majorization and
    extensions to the package 'smacof'. This package enhances 'smacof' and contains various functions, wrappers,
    methods and classes for fitting, plotting and displaying a large number of different flexible MDS models
    (some as of yet unpublished) such as Torgerson scaling (Torgerson, 1958, ISBN:978-0471879459) with powers,
    Sammon mapping (Sammon, 1969, <doi:10.1109/T-C.1969.222678>) with ratio and interval optimal scaling,
    Multiscale MDS (Ramsay, 1977, <doi:10.1007/BF02294052>) with ratio and interval optimal scaling, S-stress MDS
    (ALSCAL; Takane, Young & De Leeuw, 1977, <doi:10.1007/BF02293745>) with ratio and interval optimal
    scaling, elastic scaling (McGee, 1966, <doi:10.1111/j.2044-8317.1966.tb00367.x>) with ratio and interval
    optimal scaling, r-stress MDS (De Leeuw, Groenen & Mair, 2016, <https://rpubs.com/deleeuw/142619>) with ratio,
    interval and non-metric optimal scaling, power-stress MDS
    (POST-MDS; Buja & Swayne, 2002 <doi:10.1007/s00357-001-0031-0>) with ratio and interval optimal scaling,
    restricted power-stress (Rusch, Mair & Hornik, 2021, <doi:10.1080/10618600.2020.1869027>)
    with ratio and interval optimal scaling, approximate power-stress with ratio optimal scaling
    (Rusch, Mair & Hornik, 2021, <doi:10.1080/10618600.2020.1869027>),
    Box-Cox MDS (Chen & Buja, 2013, <https://jmlr.org/papers/v14/chen13a.html>),
    local MDS (Chen & Buja, 2009, <doi:10.1198/jasa.2009.0111>), curvilinear component analysis
    (Demartines & Herault, 1997, <doi:10.1109/72.554199>) and curvilinear distance analysis
    (Lee, Lendasse & Verleysen, 2004, <doi:10.1016/j.neucom.2004.01.007>). There also are experimental
    models (e.g., sparsified MDS and sparsified POST-MDS). Some functions are suitably flexible to allow any other
    sensible combination of explicit power transformations for weights, distances and input proximities with
    implicit ratio, interval or non-metric optimal scaling of the input proximities. Most functions use a 
    Majorization-Minimization algorithm. 
	"""
	
	homepage = "https://r-forge.r-project.org/projects/stops/"
	cran = "smacofx" 

	version("0.6-6", md5="bdbc7b6ddc4b38454ba77dfb5a0d6edc")

	depends_on("r-smacof@1.10.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-minqa", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-projectionbasedclustering", type=("build", "run"))
	depends_on("r-weights", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
