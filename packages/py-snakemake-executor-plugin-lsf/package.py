# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySnakemakeExecutorPluginLsf(PythonPackage):
	"""A Snakemake executor plugin for submitting jobs to a LSF cluster."""
	
	homepage = "https://github.com/befh/snakemake-executor-plugin-lsf"
	pypi = "snakemake-executor-plugin-lsf/snakemake_executor_plugin_lsf-0.2.6" 

	version("0.2.0", sha256="d89a22de8939ebf122bf7be6c929aea53dda51f7d03af6b5ca8bf5d638521301", expand=False, url="https://files.pythonhosted.org/packages/6e/f8/2436a55e09ba5966a6af73d7462d68f4a4dec23b936ea991156954ea3abc/snakemake_executor_plugin_lsf-0.2.0-py3-none-any.whl")
	version("0.2.1", sha256="4d1136b9f92a5cd9db63f62e80b6205b6b7950dff191fd200d65163ddd6e0889", expand=False, url="https://files.pythonhosted.org/packages/d2/24/2530091db49b39b006b237d972b64b4266ff5a81397a421eafda648f3e2d/snakemake_executor_plugin_lsf-0.2.1-py3-none-any.whl")
	version("0.2.2", sha256="085e1e83e11b541dee1bd0992f6ddc83a7c378c5cddb79b3de794bde33f423e1", expand=False, url="https://files.pythonhosted.org/packages/0e/e6/93f6a4927788b6fcc59618a46c44e81b3154ba8c7e7650b858b8b1f14934/snakemake_executor_plugin_lsf-0.2.2-py3-none-any.whl")
	version("0.2.3", sha256="19edd4b581d042ab899af76883be6604df529bc0fa872b0d4b1df3a6092d95a0", expand=False, url="https://files.pythonhosted.org/packages/6e/a3/4016ba6c21eccc8ae5a16c178fc5fbfb4503e9553575582c5e15538d994c/snakemake_executor_plugin_lsf-0.2.3-py3-none-any.whl")
	version("0.2.4", sha256="f96c319c21088e644a1391e13dc0e465f94c01a6f5a62566e2b312c96a5d5ab4", expand=False, url="https://files.pythonhosted.org/packages/4f/39/e523c626b1ceb9239ad656be63f11fe3b365535b7db284782503c257545d/snakemake_executor_plugin_lsf-0.2.4-py3-none-any.whl")
	version("0.2.5", sha256="630a51b4508daab4422047191afd7cc59c28b066ad3939a15ca1a5b8b84c0fb1", expand=False, url="https://files.pythonhosted.org/packages/71/28/74851a972cc20068b763849db705b7e95ec1f6479794255cc4ada1dbe384/snakemake_executor_plugin_lsf-0.2.5-py3-none-any.whl")
	version("0.2.6", sha256="8ddbd53c20a48c2447ff72cb65e95f3fd12b293c5f5348fc15e8a29dc8069823", expand=False, url="https://files.pythonhosted.org/packages/41/da/4a210bfa7b9bad082b084873ec122d7b65b16fe46b824c5c20dbd5af4cc2/snakemake_executor_plugin_lsf-0.2.6-py3-none-any.whl")

	depends_on("python@3.11:", type=("build", "run"))
	depends_on("py-throttler", type=("build", "run"))
	depends_on("py-snakemake-executor-plugin-lsf-jobstep", type=("build", "run"))
	depends_on("py-snakemake-interface-executor-plugins", type=("build", "run"))
	depends_on("py-snakemake-interface-common", type=("build", "run"))
