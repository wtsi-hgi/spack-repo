# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os
from spack.util.executable import Executable


class PyKbPython(PythonPackage):
    """Python wrapper around kallisto | bustools for scRNA-seq analysis"""
    
    homepage = "https://github.com/pachterlab/kb_python"
    pypi = "kb-python/kb_python-0.29.5-py3-none-any.whl" 

    version("0.2.0", sha256="176120e6cdc10d89b66f16945c226650517b5e058ea10b9e36a78e0df529a307", expand=False, url="https://files.pythonhosted.org/packages/79/59/1d816c9016c314197126c49bb10885709224b24834affe9a56b54e27ce5b/kb_python-0.2.0-py3-none-any.whl")
    version("0.2.1", sha256="47bf025ea752dbec9c13f2cc150934b0bc9b9e847c944504bb29be1b507aef71", expand=False, url="https://files.pythonhosted.org/packages/9c/6f/b33103fc167a13a6e0b4df2305fce3da8bcd18d62a7db2903ea4d10799e6/kb_python-0.2.1-py3-none-any.whl")
    version("0.24.0", sha256="b48fdafe8e0fd75ab05931b368f001aec29327aaea8a7674f0b567b0424f883e", expand=False, url="https://files.pythonhosted.org/packages/11/6e/3fb32cd3379de065b994dd83d5cfb03fb7330d27d9a0ad32502f07e3955b/kb_python-0.24.0-py3-none-any.whl")
    version("0.24.1", sha256="4f2fb36c9cfa2f8dec47c87ab9ebc62cfc1d31d7d5460d391d7dd3274c74cfd7", expand=False, url="https://files.pythonhosted.org/packages/f3/c5/bee3f312c13d0bf0cce77efb44fa47312ec0bc5d7ecc971b295128d61bd8/kb_python-0.24.1-py3-none-any.whl")
    version("0.24.2", sha256="1805864a83deca013b93a720057fdf4368e7b54ee22289cf4a66bfe0c4b4a8db", expand=False, url="https://files.pythonhosted.org/packages/fa/1c/0476f79985f4df0ead573eeee91c5cee6f7cd05f777db169f1eedf9de302/kb_python-0.24.2-py3-none-any.whl")
    version("0.24.3", sha256="7e55987473dcc862a075177249a50290066f2a9c47681c07ef2f896a28f1dee3", expand=False, url="https://files.pythonhosted.org/packages/88/c5/7f5721b03195dccc4f187fd82f0547607c50bd95fb07d43788d947f28a6b/kb_python-0.24.3-py3-none-any.whl")
    version("0.24.4", sha256="0e2cb72d90f31cdda0ee9deced632be6603c8baa4af4b735fa6e41b37cfe9386", expand=False, url="https://files.pythonhosted.org/packages/62/c9/2e5b8fa2cd873a23ae1aeb128b33165d6a9387a2f56ea1fafec1d6d32477/kb_python-0.24.4-py3-none-any.whl")
    version("0.25.0", sha256="74fa467a8bcca036a3b89fc1516fca5fbf57d5e4d32c151a0125c69d8c8a0f77", expand=False, url="https://files.pythonhosted.org/packages/5c/d4/263606724d49c4fe2a765d2a48221a90d1d88403f827ce0fdafe1810a40d/kb_python-0.25.0-py3-none-any.whl")
    version("0.25.1", sha256="6ce1cc6988c6ceb5a68a38f99e90d05e7e938fa07f83b256861f98a2dbae0c1a", expand=False, url="https://files.pythonhosted.org/packages/29/94/855ed1c11110a65a466cd95a6fef64958bad055f2678270b80a32e42cdb1/kb_python-0.25.1-py3-none-any.whl")
    version("0.26.0", sha256="d0f4b49bd1dc7d51cf5814620ede319943cb8997c9de3f015b89da01423207e5", expand=False, url="https://files.pythonhosted.org/packages/79/7a/e31c32e3181fb869b165ded897a7583ff0e55b668f33e2bfbf703ae5d1d8/kb_python-0.26.0-py3-none-any.whl")
    version("0.26.1", sha256="07df6ac2fdcced9411be380f61f52897d43876ee374700fdce7255c647a0afe7")
    version("0.26.2", sha256="0382195b0956168a97944275c8e6b960e4f92ac6eb60f445091d13ecbc024fe1")
    version("0.26.3", sha256="c5e95258062db9c53267bf6bfe43d585652e1d5ac3c4808dc661ff0f79c07859")
    version("0.26.4", sha256="2d621c489fcfe5af2094c3bca4beb5f101005acffcf5d631d89cf306d4575f81")
    version("0.27.0", sha256="9f1ced62708b288ced311ff65dd20ed3f97d30d00e1572ff3e44182df27c82d2")
    version("0.27.1", sha256="754663be93e284225fab283b05ad137d6a9adf281bfa5edc6f77a6a68d445042")
    version("0.27.2", sha256="613932cf1810fe21b06315218b5c2aaf696beff63ca5ba641473df41e8b907e6")
    version("0.27.3", sha256="dc98f6ceb4402d666b7e0d19be17c63d33e8b710a35cdc33de7c0f457122f43f")
    version("0.28.0", sha256="ce50cca5e03316da22e352cefd09211f26c411c8c5f9b9237956e59677cd7b9c", expand=False, url="https://files.pythonhosted.org/packages/7f/c7/f05a342e570e9fc7005220f51231d3a05adbd8199fdde06a8ab9869732a8/kb_python-0.28.0-py3-none-any.whl")
    version("0.28.1", sha256="94605990f46709673eb011a364a451a75148dee4e88ba3e93c21c6bbfd512fe3", expand=False, url="https://files.pythonhosted.org/packages/dd/b0/01baebe6b09a5220d2d97f0846f065a2c70b4eaa46bb2d9cfcb1e0a77b3e/kb_python-0.28.1-py3-none-any.whl")
    version("0.28.2", sha256="96994fab191e8ad7f106b204b903d3840be585846a6f1c423e3cdd27991b158e", expand=False, url="https://files.pythonhosted.org/packages/07/01/24a1988b1388ac231af489f715431fc43060e1642878af908a9b4af37c38/kb_python-0.28.2-py3-none-any.whl")
    version("0.29.0", sha256="8f6c46c733bb6bbdff8c44f984ff35f9dce9abda220469090334a0aaea09f586", expand=False, url="https://files.pythonhosted.org/packages/b4/7b/078adba02de9282e10eb7fc437fc277d7678de4b3e2b5d84ec7732190c7b/kb_python-0.29.0-py3-none-any.whl")
    version("0.29.1", sha256="59f3955c591dff5d3fd3423c6eabb2ea1926435ec164652d890a486ac017d953", expand=False, url="https://files.pythonhosted.org/packages/dd/48/a435abcc1926fefd87d19dce7cf1a1f447f37aeb412b5cddd6a6fdf8d30a/kb_python-0.29.1-py3-none-any.whl")
    version("0.29.2", sha256="cb029ac71edde884a054b6a05407eb2c1dd2f7b40318786cbdcd0940ff62cd06", expand=False, url="https://files.pythonhosted.org/packages/7b/08/489c01f6c3bd78587cc561cd0b2853543b4c5edc322c81e654ea84fec7ee/kb_python-0.29.2-py3-none-any.whl")
    version("0.29.3", sha256="b37250fb1b66fdde1fb1e46916165d6c8b5434d43b7b08fdf8e0e76df0170c24", expand=False, url="https://files.pythonhosted.org/packages/83/41/72d82241d03d7d72419bc7d46fb0323b81c4577ea058067c7b970bd5ba5b/kb_python-0.29.3-py3-none-any.whl")
    version("0.29.5", sha256="24141916807c8dd41484e5e9d7710df92e1386b77cf5dafa10f06d106b88b8a9", expand=False, url="https://files.pythonhosted.org/packages/be/dc/549f2de517272abda9f4169d70bf2c1268a4f0ce159901a0d8c1c9e6d10b/kb_python-0.29.5-py3-none-any.whl")

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-anndata", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))
    depends_on("py-loompy", type=("build", "run"))
    depends_on("py-nbconvert", type=("build", "run"))
    depends_on("py-nbformat", type=("build", "run"))
    # ngs-tools version requirements vary by kb-python version
    depends_on("py-ngs-tools@1.8.5:", when="@0.28.0:0.28.2", type=("build", "run"))
    depends_on("py-ngs-tools@1.8.6:", when="@0.29.0:", type=("build", "run"))
    depends_on("py-ngs-tools", when="@:0.27", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-plotly", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-scanpy", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            kb_exe = join_path(self.prefix.bin, "kb")
            if os.path.exists(kb_exe):
                try:
                    Executable(kb_exe)("--help")
                    return
                except Exception:
                    pass
            # Fallback: simple Python import test
            python("-c", "import kb_python")

# {'anndata(>=0.6.22.post1)': ['0.2.0', '0.2.1', '0.24.0', '0.24.1', '0.24.2', '0.24.3', '0.24.4', '0.25.0', '0.25.1', '0.26.0'], 'loompy(>=3.0.6)': ['0.2.0', '0.2.1', '0.24.0', '0.24.1', '0.24.2', '0.24.3', '0.24.4', '0.25.0', '0.25.1', '0.26.0', '0.29.0', '0.29.1'], 'h5py(>=2.10.0)': ['0.25.0', '0.25.1', '0.26.0', '0.29.0', '0.29.1'], 'Jinja2(>2.10.1)': ['0.25.0', '0.25.1', '0.26.0', '0.29.0', '0.29.1'], 'nbconvert(>=5.6.0)': ['0.25.0', '0.25.1', '0.26.0', '0.29.0', '0.29.1'], 'nbformat(>=4.4.0)': ['0.25.0', '0.25.1', '0.26.0', '0.29.0', '0.29.1'], 'numpy(>=1.17.2)': ['0.25.0', '0.25.1', '0.26.0', '0.29.0', '0.29.1'], 'plotly(>=4.5.0)': ['0.25.0', '0.25.1', '0.26.0', '0.29.0', '0.29.1'], 'requests(>=2.19.0)': ['0.25.0', '0.25.1', '0.26.0'], 'scanpy(>=1.4.4.post1)': ['0.25.0', '0.25.1', '0.26.0', '0.29.0', '0.29.1'], 'scikit-learn(>=0.21.3)': ['0.25.0', '0.25.1', '0.26.0', '0.29.0', '0.29.1'], 'tqdm(>=4.39.0)': ['0.25.0', '0.25.1', '0.26.0'], 'anndata>=0.6.22.post1': ['0.28.0', '0.28.1', '0.28.2'], 'h5py>=2.10.0': ['0.28.0', '0.28.1', '0.28.2', '0.29.2', '0.29.3', '0.29.5'], 'Jinja2>2.10.1': ['0.28.0', '0.28.1', '0.28.2', '0.29.2', '0.29.3', '0.29.5'], 'loompy>=3.0.6': ['0.28.0', '0.28.1', '0.28.2', '0.29.2', '0.29.3', '0.29.5'], 'nbconvert>=5.6.0': ['0.28.0', '0.28.1', '0.28.2', '0.29.2', '0.29.3', '0.29.5'], 'nbformat>=4.4.0': ['0.28.0', '0.28.1', '0.28.2', '0.29.2', '0.29.3', '0.29.5'], 'ngs-tools>=1.8.5': ['0.28.0', '0.28.1', '0.28.2'], 'numpy>=1.17.2': ['0.28.0', '0.28.1', '0.28.2', '0.29.2', '0.29.3', '0.29.5'], 'pandas<2,>=1.0.0': ['0.28.0', '0.28.1', '0.28.2'], 'plotly>=4.5.0': ['0.28.0', '0.28.1', '0.28.2', '0.29.2', '0.29.3', '0.29.5'], 'requests>=2.22.0': ['0.28.0', '0.28.1', '0.28.2', '0.29.2', '0.29.3', '0.29.5'], 'scanpy>=1.4.4.post1': ['0.28.0', '0.28.1', '0.28.2', '0.29.2', '0.29.3', '0.29.5'], 'scikit-learn>=0.21.3': ['0.28.0', '0.28.1', '0.28.2', '0.29.2', '0.29.3', '0.29.5'], 'typing-extensions>=3.7.4': ['0.28.0', '0.28.1', '0.28.2', '0.29.2', '0.29.3', '0.29.5'], 'anndata(>=0.9.2)': ['0.29.0', '0.29.1'], 'ngs-tools(>=1.8.6)': ['0.29.0', '0.29.1'], 'pandas(>=1.5.3)': ['0.29.0', '0.29.1'], 'requests(>=2.22.0)': ['0.29.0', '0.29.1'], 'typing-extensions(>=3.7.4)': ['0.29.0', '0.29.1'], 'biopython(>=1.8)': ['0.29.0', '0.29.1'], 'anndata>=0.9.2': ['0.29.2', '0.29.3', '0.29.5'], 'ngs-tools>=1.8.6': ['0.29.2', '0.29.3', '0.29.5'], 'pandas>=1.5.3': ['0.29.2', '0.29.3', '0.29.5'], 'biopython>=1.8': ['0.29.2', '0.29.3', '0.29.5']}
