import os
import yaml
import markdown
import bleach

POST_DIR = os.path.join(os.path.dirname(__file__), 'posts')


def load_posts(post_id):
    """
    Carrega um único post pelo seu ID.
    Retorna um dicionário com metadata + conteúdo em HTML + id.
    """
    for filename in os.listdir(POST_DIR):
        if filename.startswith(f'{post_id:03}') and filename.endswith(".md"):
            path = os.path.join(POST_DIR, filename)

            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Separar front-matter do corpo
            parts = content.split('---', 2)
            if len(parts) < 3:
                raise ValueError(f"O post {filename} não tem front-matter válido")

            _, meta, body = parts

            metadata = yaml.safe_load(meta) or {}

            html = markdown.markdown(
                body,
                extensions=["fenced_code", "codehilite", "toc", "tables"]
            )

            



            # Retorna post completo
            return {
                **metadata,
                "content": html,
                "id": metadata.get("id", post_id),
            }

    return None


def load_all_posts_sorted():
    """
    Carrega todos os posts da pasta, converte Markdown para HTML
    e ordena por id do maior (mais recente) para o menor.
    """
    posts = []
    for filename in os.listdir(POST_DIR):
        if filename.endswith(".md"):
            path = os.path.join(POST_DIR, filename)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Separar front-matter
            parts = content.split('---', 2)
            if len(parts) < 3:
                # Caso não tenha front-matter, só converte Markdown
                html = markdown.markdown(content, extensions=["fenced_code", "codehilite", "toc"])
                posts.append({"filename": filename, "content": html, "id": 0})
                continue

            _, meta, body = parts
            metadata = yaml.safe_load(meta) or {}
            html = markdown.markdown(body, extensions=["fenced_code", "codehilite", "toc"])

            posts.append({
                **metadata,
                "content": html,
                "id": metadata.get("id", 0)
            })

    # Ordenar pelo id do maior (mais recente) para o menor
    posts_sorted = sorted(posts, key=lambda x: x.get("id", 0), reverse=True)
    return posts_sorted


# Inicializa lista global de posts já ordenada
all_posts = load_all_posts_sorted()

# Debug: mostrar todos os posts carregados
if __name__ == "__main__":
    for post in all_posts:
        print(f"ID: {post.get('id')} - Título: {post.get('title')}")
