# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMultiprocessingOnDill(PythonPackage):
    """This project is a friendly fork – for Python 3 – of the Python Standard Library multiprocessing module, which uses the third-party dill serializer instead of the standard pickle serializer. This overcomes many shortcomings of pickle which prevent multiprocessing being used with lambdas, closures and other useful Python objects."""

    homepage = "https://github.com/sixty-north/multiprocessing_on_dill"
    pypi = "multiprocessing_on_dill/multiprocessing_on_dill-3.5.0a4.tar.gz"

    version("3.5.0a4", sha256="d6d50c300ff4bd408bb71eb78725e60231039ee9b3d0d9bb7697b9d0e15045e7")

    depends_on("py-setuptools", type="build")
