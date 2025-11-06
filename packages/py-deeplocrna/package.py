# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDeeplocrna(PythonPackage):
    """Predicting RNA localization based on RBP binding information.

    Note: The published PyPI artifacts for DeepLocRNA are wheel-only and act
    as a meta-package (no importable modules). We install from the wheel and
    rely on Spack to provide the declared runtime dependencies.
    """

    homepage = "https://github.com/TerminatorJ/DeepLocRNA"
    pypi = "DeepLocRNA/DeepLocRNA-0.0.4-py3-none-any.whl"

    # Wheel-only releases
    version(
        "0.0.3",
        sha256="316bd7163ca4e2b134db36f3c5103c3203bb759dd28075647153abbecde65d47",
        expand=False,
        url="https://files.pythonhosted.org/packages/e8/03/357731f7431e5736419b36daa57dd5b6261dcaf3af6c67b0fb998e39cab5/DeepLocRNA-0.0.3-py3-none-any.whl",
    )
    version(
        "0.0.4",
        sha256="45866048e8360f14907462bda1e36987ec056e90b7ea4f290c7178538f9e416d",
        expand=False,
        url="https://files.pythonhosted.org/packages/59/79/c3df085eeba8e6483e4163e2175cef89f7025d4ef1542eb2bcddc139742f/DeepLocRNA-0.0.4-py3-none-any.whl",
    )

    # Build requirements provided by the python_pip builder via PythonPackage
    depends_on("py-setuptools", type=("build",))

    # Runtime requirements (based on PyPI metadata). Keep unpinned to allow
    # Spack to resolve compatible versions; gate version-specific extras.
    depends_on("py-captum", type=("build", "run"))
    depends_on("py-gin-config", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-keras", type=("build", "run"))
    depends_on("py-logomaker", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-pillow", type=("build", "run"))
    depends_on("py-pytorch-lightning", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-torch", type=("build", "run"))
    depends_on("py-torchinfo", type=("build", "run"))
    depends_on("py-torchsummary", type=("build", "run"))
    depends_on("py-torchvision", type=("build", "run"))
    depends_on("py-wandb", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-typing-extensions", when="@0.0.4:", type=("build", "run"))
    depends_on("py-tensorflow", when="@0.0.4:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        # The wheel contains no modules; validate distribution metadata exists.
        with working_dir("spack-test", create=True):
            python(
                "-c",
                (
                    "import importlib, sys; "
                    "from importlib.metadata import distribution; "
                    "distribution('DeepLocRNA'); print('DeepLocRNA present')"
                ),
            )

# PyPI requirements summary (for reference):
# {'captum==0.6.0': ['0.0.3'], 'gin-config==0.5.0': ['0.0.3'], 'h5py==2.10.0': ['0.0.3'],
#  'Keras==2.2.4': ['0.0.3'], 'logomaker==0.8': ['0.0.3'], 'numpy==1.19.5': ['0.0.3'],
#  'pandas==1.4.4': ['0.0.3'], 'Pillow==9.4.0': ['0.0.3'], 'pytorch-lightning==1.9.4': ['0.0.3'],
#  'scikit-learn==1.0.2': ['0.0.3'], 'torch==1.13.1': ['0.0.3'], 'torchinfo==1.7.2': ['0.0.3'],
#  'torchsummary==1.5.1': ['0.0.3'], 'torchvision==0.14.1': ['0.0.3'], 'wandb==0.14.0': ['0.0.3'],
#  'matplotlib==3.6.3': ['0.0.3'], 'captum(==0.6.0)': ['0.0.4'], 'gin-config(==0.5.0)': ['0.0.4'],
#  'h5py(==2.10.0)': ['0.0.4'], 'Keras(==2.2.4)': ['0.0.4'], 'logomaker(==0.8)': ['0.0.4'],
#  'numpy(==1.19.5)': ['0.0.4'], 'pandas(==1.4.4)': ['0.0.4'], 'Pillow(==9.4.0)': ['0.0.4'],
#  'pytorch-lightning(==1.9.4)': ['0.0.4'], 'scikit-learn(==1.0.2)': ['0.0.4'],
#  'torch(==1.13.1)': ['0.0.4'], 'torchinfo(==1.7.2)': ['0.0.4'], 'torchsummary(==1.5.1)': ['0.0.4'],
#  'torchvision(==0.14.1)': ['0.0.4'], 'wandb(==0.14.0)': ['0.0.4'], 'matplotlib(==3.6.3)': ['0.0.4'],
#  'tensorflow(==2.4.1)': ['0.0.4'], 'typing-extensions(==4.7.1)': ['0.0.4']}
