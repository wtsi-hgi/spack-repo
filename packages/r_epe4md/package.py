# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpe4md(RPackage):
	"""EPE's 4MD Model to Forecast the Adoption of Distributed
Generation

	EPE's (Empresa de Pesquisa Energética) 4MD (Modelo de Mercado da Micro e Minigeração Distribuída - Micro and Mini Distributed Generation Market Model) model to forecast the adoption of Distributed Generation. Given the user's assumptions, it is possible to estimate how many consumer units will have distributed generation in Brazil over the next 10 years, for example. In addition, it is possible to estimate the installed capacity, the amount of investments that will be made in the country and the monthly energy contribution of this type of generation. <https://www.epe.gov.br/sites-pt/publicacoes-dados-abertos/publicacoes/PublicacoesArquivos/publicacao-689/topico-639/NT_Metodologia_4MD_PDE_2032_VF.pdf>.
	"""
	
	homepage = "https://epe-gov-br.github.io/epe4md/"
	cran = "epe4md" 

	version("0.1.4", md5="3f54c0f22678ee4c31c91b892fee5e25")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1.1.1:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-jrvfinance", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-tsibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-fabletools", type=("build", "run"))
	depends_on("r-feasts", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
