import { ContentCard } from '@/components/ContentCard';
import api from '@/lib/api';

export default async function Home() {
  const content = await api.get('/content/search').then(res => res.data);
  
  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-4xl font-bold mb-8">Популярное</h1>
        <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
          {content.map((item) => (
            <ContentCard key={item.id} content={item} />
          ))}
        </div>
      </div>
    </div>
  );
}