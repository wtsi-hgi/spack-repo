# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBioemu(PythonPackage):
    """Biomolecular emulator"""
    
    homepage = "https://github.com/microsoft/bioemu"
    pypi = "bioemu/bioemu-1.1.0-py3-none-manylinux1_x86_64.whl" 

    version("0.1.0", sha256="1c44bd8aa548407f30f63fcf33bff30d11d7ee6b9f8dad5f99054eceb9e417ee", expand=False, url="https://files.pythonhosted.org/packages/7f/73/385b4d0f12526f07e057d9376aac3cb9e1330645a8f19f152b66449673c2/bioemu-0.1.0-py3-none-any.whl")
    version("0.1.10", sha256="53e4560a875b544c3184052eae00b1a07c955bb1d64c61965e6ed59b0d4f788d", expand=False, url="https://files.pythonhosted.org/packages/c4/29/42248a4517def4edbace87379eff5c791872ba3125c095e6b661fbff5740/bioemu-0.1.10-py3-none-manylinux1_x86_64.whl")
    version("0.1.11", sha256="ab8f293599c6f29ea6803446131174398cd30c394af2b88b4239cff49b72e594", expand=False, url="https://files.pythonhosted.org/packages/81/1a/44fe3508ed114ccd4b112851968e2d9755feda4d6573cd6dbfa65d44a6ec/bioemu-0.1.11-py3-none-manylinux1_x86_64.whl")
    version("0.1.12", sha256="f779febc0cb10eb1d92fdc01c7445b6c331ada0a5370c9101bc62ce452d4fbb5", expand=False, url="https://files.pythonhosted.org/packages/fd/60/d61399cac78141e169a4d75c08ac8f090e2ec5abed933d05fe3d9f2d7095/bioemu-0.1.12-py3-none-manylinux1_x86_64.whl")
    version("0.1.2", sha256="89eff788ba90d0a4f0ed9d69b86e12750499853d814d35afbf8ede7a23835a78", expand=False, url="https://files.pythonhosted.org/packages/1a/0f/aefef09b86846f3f1cd1b4fa80303f56a368fcba8e4ad1d64cd68b29fd30/bioemu-0.1.2-py3-none-any.whl")
    version("0.1.3", sha256="ae4077f9e2de9fa50246a179a1039610bd0f6b846da6462bf219e325ef2931a4", expand=False, url="https://files.pythonhosted.org/packages/17/75/32569c710c9e16d898da69948b405253de8fd75196215f98990bbabb01f0/bioemu-0.1.3-py3-none-manylinux1_x86_64.whl")
    version("0.1.4", sha256="93aedaa8c3802b0a55137ae9bba57bdb7f01f6e0fe9d71ad939f7e89feba2674", expand=False, url="https://files.pythonhosted.org/packages/06/7b/23c1629b9497c71202d2cd1fed491b86b0d6e5e9d60cad3ee5fc21814832/bioemu-0.1.4-py3-none-manylinux1_x86_64.whl")
    version("0.1.5", sha256="196de8fd4d6c1cd6ed02b76f52a89a1da97e547da68c4b34fa880f562b62443d", expand=False, url="https://files.pythonhosted.org/packages/65/1b/2918674f25fbfa623f21680cb080245cd879cfe7633eb0a44e24c0ab021c/bioemu-0.1.5-py3-none-manylinux1_x86_64.whl")
    version("0.1.5a1", sha256="84582c979f67ffe9a559f6525fa89ac3eb97b2f143c626d4a4be238420751c06", expand=False, url="https://files.pythonhosted.org/packages/b3/ea/2b1ad9ca3235573f8567e8f9cbf22cf2410ecb846cc8b98dd297763b7d73/bioemu-0.1.5a1-py3-none-manylinux1_x86_64.whl")
    version("0.1.5a2", sha256="148402fd3a5a34043d3bf8e3e22fe323e8ad92ecae16c84338ac11de4d8bda5a", expand=False, url="https://files.pythonhosted.org/packages/49/c1/01704b3d4b4f35aef31a3822cbc552455d652bc201106ebebc63bd7048a4/bioemu-0.1.5a2-py3-none-manylinux1_x86_64.whl")
    version("0.1.5a3", sha256="c0c2ebda3a6db87a28e431d3d89ea7333fb0d2d9f0c8b49f2826f8e19956c263", expand=False, url="https://files.pythonhosted.org/packages/4a/5c/48400b7d17dee46f12e8cad7eac08ff97f20282c6383e17076ee2df15321/bioemu-0.1.5a3-py3-none-manylinux1_x86_64.whl")
    version("0.1.5a4", sha256="feaf58f48008b771ff556f832ca57f0ad7629e2df90dc9c87d2d0ce7000a28d5", expand=False, url="https://files.pythonhosted.org/packages/c0/fa/cc9f2e4b1f56f9dd9daa684ddafed96124fa92dea97781e6f62e4514db5f/bioemu-0.1.5a4-py3-none-manylinux1_x86_64.whl")
    version("0.1.6", sha256="03bfe3e920fc7d1a54145005c3dc0637d044b5255948a6d3a7bf88676eb19a56", expand=False, url="https://files.pythonhosted.org/packages/99/fe/d58cb9d216a0c73b7747aa98788585efe09d021cf7f60e91cb324aebdb89/bioemu-0.1.6-py3-none-manylinux1_x86_64.whl")
    version("0.1.7", sha256="81c9311ea6b8dfd76a68ae1ae2e7c26ca3ca059b89307208c6f699f1c6aaec57", expand=False, url="https://files.pythonhosted.org/packages/be/83/235999d0a926b965f30374c2206c75b371a46d93eeb67ec76016526380da/bioemu-0.1.7-py3-none-manylinux1_x86_64.whl")
    version("0.1.8", sha256="ca56354140f4d16b1fb62d278f1ce6156e7eb7e02f04e5052d176d3b23a1f0e3", expand=False, url="https://files.pythonhosted.org/packages/bd/d5/02d58f59f3c75dbcbbb761727fb16f48504266c13e94390add230e9b92b7/bioemu-0.1.8-py3-none-manylinux1_x86_64.whl")
    version("0.1.9", sha256="19d6e4ba47b31d2a00ff894019761e1a5258470af27205b7d62d5ab25e9bd0d6", expand=False, url="https://files.pythonhosted.org/packages/0f/37/d7d918c6704886f5e37fe3dca74e7ba783e6c48117a635c046d7aee56694/bioemu-0.1.9-py3-none-manylinux1_x86_64.whl")
    version("1.1.0", sha256="0cffc54af104a87c42eb1c5983382586530d6f87efbf1b234771d694e973bddf", expand=False, url="https://files.pythonhosted.org/packages/c6/28/9dfa63cc5c863948660bc7ffebc723382ad32f29d7de02f5e0384c119b31/bioemu-1.1.0-py3-none-manylinux1_x86_64.whl")

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-mdtraj", type=("build", "run"))
    depends_on("py-torch-geometric", type=("build", "run"))
    depends_on("py-torch", type=("build", "run"))
    depends_on("py-modelcif", type=("build", "run"))
    depends_on("py-bio", type=("build", "run"))
    depends_on("py-fire", type=("build", "run"))
    depends_on("py-huggingface-hub", type=("build", "run"))
    depends_on("py-hydra-core", type=("build", "run"))
    depends_on("py-dm-tree", type=("build", "run"))
    depends_on("py-stackprinter", type=("build", "run"))
    depends_on("py-typer", type=("build", "run"))
    depends_on("py-uv", type=("build", "run"))

# {'mdtraj>=1.9.9': ['0.1.0', '0.1.10', '0.1.11', '0.1.12', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.5a1', '0.1.5a2', '0.1.5a3', '0.1.5a4', '0.1.6', '0.1.7', '0.1.8', '0.1.9', '1.1.0'], 'torch_geometric==2.6.1': ['0.1.0', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.5a1', '0.1.5a2', '0.1.5a3', '0.1.5a4', '0.1.6', '0.1.7'], 'torch==2.4.0': ['0.1.0', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.5a1', '0.1.5a2', '0.1.5a3', '0.1.5a4', '0.1.6', '0.1.7'], 'torchvision': ['0.1.0', '0.1.2', '0.1.3', '0.1.4'], 'modelcif==0.7': ['0.1.0', '0.1.10', '0.1.11', '0.1.12', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.5a1', '0.1.5a2', '0.1.5a3', '0.1.5a4', '0.1.6', '0.1.7', '0.1.8', '0.1.9', '1.1.0'], 'bio>=1.5.9': ['0.1.0', '0.1.10', '0.1.11', '0.1.12', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.5a1', '0.1.5a2', '0.1.5a3', '0.1.5a4', '0.1.6', '0.1.7', '0.1.8', '0.1.9', '1.1.0'], 'fire==0.7.0': ['0.1.0', '0.1.10', '0.1.11', '0.1.12', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.5a1', '0.1.5a2', '0.1.5a3', '0.1.5a4', '0.1.6', '0.1.7', '0.1.8', '0.1.9', '1.1.0'], 'huggingface-hub': ['0.1.0', '0.1.10', '0.1.11', '0.1.12', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.5a1', '0.1.5a2', '0.1.5a3', '0.1.5a4', '0.1.6', '0.1.7', '0.1.8', '0.1.9', '1.1.0'], 'hydra-core': ['0.1.0', '0.1.10', '0.1.11', '0.1.12', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.5a1', '0.1.5a2', '0.1.5a3', '0.1.5a4', '0.1.6', '0.1.7', '0.1.8', '0.1.9', '1.1.0'], 'dm-tree': ['0.1.0', '0.1.10', '0.1.11', '0.1.12', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.5a1', '0.1.5a2', '0.1.5a3', '0.1.5a4', '0.1.6', '0.1.7', '0.1.8', '0.1.9', '1.1.0'], 'stackprinter': ['0.1.0', '0.1.10', '0.1.11', '0.1.12', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.5a1', '0.1.5a2', '0.1.5a3', '0.1.5a4', '0.1.6', '0.1.7', '0.1.8', '0.1.9', '1.1.0'], 'typer': ['0.1.0', '0.1.10', '0.1.11', '0.1.12', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.5a1', '0.1.5a2', '0.1.5a3', '0.1.5a4', '0.1.6', '0.1.7', '0.1.8', '0.1.9', '1.1.0'], 'pytest;extra=="dev"': ['0.1.0', '0.1.10', '0.1.11', '0.1.12', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.5a1', '0.1.5a2', '0.1.5a3', '0.1.5a4', '0.1.6', '0.1.7', '0.1.8', '0.1.9', '1.1.0'], 'pytest-cov;extra=="dev"': ['0.1.0', '0.1.10', '0.1.11', '0.1.12', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.5a1', '0.1.5a2', '0.1.5a3', '0.1.5a4', '0.1.6', '0.1.7', '0.1.8', '0.1.9', '1.1.0'], 'pre-commit;extra=="dev"': ['0.1.0', '0.1.10', '0.1.11', '0.1.12', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.5a1', '0.1.5a2', '0.1.5a3', '0.1.5a4', '0.1.6', '0.1.7', '0.1.8', '0.1.9', '1.1.0'], 'openmm==8.2.0;extra=="md"': ['0.1.0', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.5a1', '0.1.5a2', '0.1.5a3', '0.1.5a4', '0.1.6', '0.1.7'], 'pdb2pqr==3.4.1;extra=="md"': ['0.1.0', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.5a1', '0.1.5a2', '0.1.5a3', '0.1.5a4', '0.1.6', '0.1.7'], 'torch_geometric>=2.6.1': ['0.1.10', '0.1.11', '0.1.12', '0.1.8', '0.1.9', '1.1.0'], 'torch>=2.6.0': ['0.1.10', '0.1.11', '0.1.12', '0.1.8', '0.1.9', '1.1.0'], 'openmm[cuda12]==8.2.0;extra=="md"': ['0.1.10', '0.1.11', '0.1.12', '0.1.8', '0.1.9', '1.1.0'], 'uv': ['0.1.12', '1.1.0']}