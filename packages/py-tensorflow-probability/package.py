# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTensorflowProbability(PythonPackage):
    """TensorFlow Probability is a Python library for probabilistic reasoning
    and statistical analysis built on TensorFlow.
    """

    homepage = "https://www.tensorflow.org/probability"
    pypi = "tensorflow-probability/tensorflow_probability-0.12.1-py2.py3-none-any.whl"

    version(
        "0.12.1",
        sha256="f148a876671f132c931275e60156892326dcf148c7a0ea2959e7714776788fb0",
        expand=False,
        url="https://files.pythonhosted.org/packages/54/4e/c5730f3def2b4c13c632df15622f89dd6c8c019ef1062cd0fe42542d0d4c/tensorflow_probability-0.12.1-py2.py3-none-any.whl",
    )

    depends_on("python@3.6:3.9", type=("build", "run"))
    depends_on("py-pip", type="build")
    depends_on("py-setuptools", type="build")

    depends_on("py-six@1.10:", type=("build", "run"))
    depends_on("py-numpy@1.13.3:", type=("build", "run"))
    depends_on("py-decorator", type=("build", "run"))
    depends_on("py-cloudpickle@1.3:", type=("build", "run"))
    depends_on("py-gast@0.3.2:", type=("build", "run"))
    depends_on("py-dm-tree", type=("build", "run"))
    depends_on("py-tensorflow@2.4:", type=("build", "run"))
