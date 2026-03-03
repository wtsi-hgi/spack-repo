# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLoggingExceptions(PythonPackage):
	"""Self-logging exceptions: Attach log messages to exceptions and output them conditionally."""
	
	homepage = "https://github.com/Bernhard10/logging_exceptions"
	pypi = "logging-exceptions/logging_exceptions-0.1.9.tar.gz" 

	version("0.1.4", sha256="4254b82b5ee13e8dc12caeb9eea9391f321b98daf6650911cd52ed8b575fa420", expand=False, url="https://files.pythonhosted.org/packages/fd/db/f67ea893b76ce3508f61eb4c456c7bc77f94a7cdc197d5ee53f5f4df9499/logging_exceptions-0.1.4-py2.py3-none-any.whl")
	version("0.1.5", sha256="6be9512f92ded4911e30ef80e5e1db51a1dabc8196bd351334bd24ff2977a382", expand=False, url="https://files.pythonhosted.org/packages/b2/1a/b958c17050acc6116b3b030cf0ef06cad7a15a3b59214204d33e5e06a48d/logging_exceptions-0.1.5-py2.py3-none-any.whl")
	version("0.1.6", sha256="b9d2f8148a73efd416335a646c52fb216177a4be23c1adb179da1c45dc68564c", expand=False, url="https://files.pythonhosted.org/packages/a9/20/ce22ce747c89a56905944b664c863de39968ec41aaecdf2ae9f49ba79a7c/logging_exceptions-0.1.6-py2.py3-none-any.whl")
	version("0.1.7", sha256="acc19fd2ab2921101216a67fe3d355bcde8f9223d512bfc6d1b0f2c71cec9ba4", expand=False, url="https://files.pythonhosted.org/packages/64/28/bf90b0cd5d90dbbab9fd166c0b50b69a054770b23a8c114885ad2db94051/logging_exceptions-0.1.7-py2.py3-none-any.whl")
	version("0.1.8", sha256="e0d2ba8d266f9e258b5cbc117c6264128883c5ba17605c83f3818f9f8e6a4b02", expand=False, url="https://files.pythonhosted.org/packages/9c/d8/6d94dfd3bba77c4e2a4eb749291125018a010b1ac7fdee811074e7a4b73c/logging_exceptions-0.1.8-py2.py3-none-any.whl")
	version("0.1.9", sha256="e2d94aa02372389229a2eee2d5b985201b72cb1e860bf8cbee3209cbbc125819")

	depends_on("py-setuptools", type=("build"))
