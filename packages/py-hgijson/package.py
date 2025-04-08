# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHgijson(PythonPackage):
    """A Python 3 library for easily JSON encoding/decoding complex class-based Python models, using an arbitrarily complex (but easy to write!) mapping schema."""

    homepage = "https://github.com/wtsi-hgi/python-json"
    pypi = "hgijson/hgijson-1.3.1.tar.gz"

    version("3.1.0", sha256="1ac523eb5d2dc55d28000a4a493f279a45e39ba5c70fc91a738f2c7d8f220d76")
    version("1.3.1", sha256="bad7bcb68b07b2093f55528c1fd24046e06bf7e79ec3137b2e3c30da862bbd71")

    depends_on("py-setuptools", type=("build"))
    depends_on("py-python-dateutil@2.5.3:", type=("build", "run"))
