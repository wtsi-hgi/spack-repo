# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatastudio(RPackage):
	"""The Research Data Warehouse of Miguel de Carvalho

	Pulls together a collection of datasets from Miguel de Carvalho research articles. Including, for example:
    - de Carvalho (2012) <doi:10.1016/j.jspi.2011.08.016>;
    - de Carvalho et al (2012) <doi:10.1080/03610926.2012.709905>;
    - de Carvalho et al (2012) <doi:10.1016/j.econlet.2011.09.007>);
    - de Carvalho and Davison (2014) <doi:10.1080/01621459.2013.872651>;
    - de Carvalho and Rua (2017) <doi:10.1016/j.ijforecast.2015.09.004>.
	"""
	
	homepage = "https://www.maths.ed.ac.uk/~mdecarv/"
	cran = "DATAstudio" 

	version("1.1", md5="fdbb48dca97dce11a5bc7b51ae8c665e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
